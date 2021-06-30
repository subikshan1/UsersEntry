"""modules"""
import json
from datetime import date, datetime
from django.shortcuts import render
from .forms import Registration
from .models import Users, Response
from .json import python_string


# Create your views here.

# pylint: disable=too-many-locals
def index(request):
    """form data"""
    if request.method == "POST":
        valid = False
        form_data = Registration(request.POST)
        # pylint: disable=unused-variable
        if form_data.is_valid():
            first_name = form_data.cleaned_data['FirstName']
            last_name = form_data.cleaned_data['LastName']
            data_birth = index2(form_data.cleaned_data['DOB'])
            get_gender = gender_data(form_data.cleaned_data['Gender'])
            get_nation = get_nationality(form_data.cleaned_data['National'])
            get_city(form_data.cleaned_data['City'])
            get_pin(form_data.cleaned_data['Pin'])
            state_data = get_state(form_data.cleaned_data['State'])
            get_qualification(form_data.cleaned_data['Qualification'])
            salary_data = get_salary(form_data.cleaned_data['Salary'])
            get_pan = pan_number(form_data.cleaned_data['PanNum'])
            validate_age = validate_date(data_birth, get_gender)
            validate_data = validate_pan(get_pan)
            # Date = datetime.now()
            # form_data.cleaned_data['Date'] = Date
            count, validate = validate_all_data(data_birth, validate_age,
                                                validate_data, state_data, salary_data, get_nation)
            form_data.save()
            if isinstance(count, int):
                response = "Success"
                reason = validate
                valid = True
                result = Response(Response=response, Reason=reason)
                result.save()
            else:
                response = count
                reason = validate
                result = Response(Response=response, Reason=reason)
                result.save()
            context = {"form": form_data, "Valid": valid, "Response": reason, "Reason": response}
            return render(request, 'main/index3.html', context)

    else:
        form_data = Registration()
    context = {"form": form_data}
    return render(request, 'main/index2.html', context)


def index2(age):
    """format"""
    formate = "%Y-%m-%d"
    try:
        datetime.strptime(age, formate)
        born = datetime.strptime(age, formate).date()
        today = date.today()
        age_result = today.year \
                     - born.year - ((today.month, today.day) < (born.month, born.day))

    # pylint: disable=bare-except
    except:
        age_result = "Format should be %Y-%m-%d"

    return age_result


def get_nationality(nation):
    """Get Nationality"""
    list1 = ["Indian", "American"]
    str1 = []
    if nation in list1:
        str1.append(nation)
    else:
        str1.append("Enter valid nationality")

    print(str1[0])
    return str1[0]


def gender_data(gender):
    """Gender Details"""
    gender_list = []
    # pylint: disable=consider-using-in
    if gender == 'Male' or gender == 'Female':
        gender_list.append(gender)
    else:
        gender_list.append("Not a Valid") if gender_list == [] else gender_list
    return gender_list[0]


def get_city(city):
    """Get City"""
    city = city.lower()
    city = city.capitalize()
    return city


def get_pin(pin):
    """Get Pin"""
    return pin


def get_state(state):
    """get State"""
    state_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam",
                  "Bihar", "Chhattisgarh", "Karnataka",
                  "Madhya Pradesh", "Odisha", "Tamil Nadu",
                  "Telangana", "West Bengal"]
    state_data = []
    if state in state_list:
        state_data.append(state)
    else:
        state_data.append("State not present")
    return state_data[0]


def get_qualification(qualification):
    """Get Qualification"""
    return qualification


def get_salary(salary):
    """Get Salary"""
    salary_list = []
    if ((int(salary) > 10000)
            and (int(salary) < 90000)):
        salary_list.append(salary)

    else:
        salary_list.append("Salary from 11,000 to 89,000")
    return salary_list[0]


def pan_number(pan):
    """Get Pan"""
    return pan


def validate_date(birth, gender):
    """Get Validate"""
    gender_list = []
    # age_list = []
    birth_type = isinstance(birth, int)
    if birth_type:
        dob = birth
        g_data = gender
        if ((g_data == 'Male' and dob > 21) or
                (g_data == 'Female' and dob > 18)):
            gender_list.append("Success")

        else:
            gender_list.append("Invalid Input for DOB")

    gender_list.append("Format should be %Y-%m-%d")
    return gender_list[0]


def validate_pan(pan_num):
    """validate Pan"""
    dates = []
    validate_result = []
    # pylint: disable=no-member
    for p_data in Users.objects.raw('SELECT id,PanNum,Date FROM main_users'):
        if pan_num == p_data.PanNum:
            str1 = ''.join(str(p_data.Date))
            str1 = str1.split()
            dates.append(str1)

    if len(dates) > 0:
        dates.reverse()
        date_formate = '%Y-%m-%d'
        get_date = date.today()
        d1_data = get_date.strftime(date_formate)
        print(d1_data)
        a_data = datetime.strptime(d1_data, date_formate)
        b_data = datetime.strptime(dates[0][0], date_formate)
        delta = a_data - b_data
        delta = abs(delta)

        # pylint: disable=expression-not-assigned
        validate_result.append("Activity in last five days") \
            if delta.days <= 5 else validate_result.append("Validate Success")

        print(validate_result)

    else:
        validate_result.append("New User")
    return validate_result[0]


# pylint: disable=too-many-return-statements
# pylint: disable=too-many-arguments
def validate_all_data(birth, date_validate,
                      pan_activity, state,
                      salary, nation):
    """validate result"""
    count_validate = 0
    # pylint: disable=no-member
    json_data = json.loads(python_string)
    if birth != "Format should be %Y-%m-%d":
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['DReason'])
        return json_data['InvalidResponse'], json_data['DReason']
    # pylint: disable=consider-using-in
    if date_validate == "Success" or date_validate == 'Format should be %Y-%m-%d':
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['DReason'])
        return json_data['AResponse'], json_data['AReason']
    # pylint: disable=consider-using-in
    if pan_activity == "Validate Success" or pan_activity == "New User":
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
        return json_data['AResponse'], json_data['PanReason']

    if state != "State not present":
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
        return json_data['AResponse'], json_data['StateError']

    if salary != "Salary from 11,000 to 89,000":
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
        return json_data['AResponse'], json_data['Salary']

    if nation != "Enter valid nationality":
        count_validate += 1

    else:
        # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
        return json_data['AResponse'], json_data['Nation']

    return count_validate, "Success"


def display_user(request):
    """display data"""
    # pylint: disable=no-member
    data = Users.objects.all()
    context = {"data": data}
    return render(request, 'main/index4.html', context)
