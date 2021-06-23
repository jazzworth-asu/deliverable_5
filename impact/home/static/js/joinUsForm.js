function submitJoinUsForm() {
    
    signInFormIsValid = true

    resetJoinUsForm() 

    let middleName = $("#middleName").val()
    
    // Gender
    let gender = $('#gender').val()
    if (gender.length === 0) {
        $('#genderRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // State
    let state = $('#state').val();
    if (state.length === 0) {
        $('#stateRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // Street address
    let streetAddress = $("#streetAddress").val()
    if (streetAddress.length === 0) {
        $('#streetAddressRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // City
    let city = $("#city").val()
    if (city.length === 0) {
        $('#cityRequired').removeClass('d-none')
    }
    if (digitExistsInValue(city)) {
        $('#cityDigit').removeClass('d-none')

        signInFormIsValid = false
    }

    // Zipcode
    let zipcode = $("#zipcode").val()
    if (zipcode.length === 0) {
        $('#zipCodeRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // Cell
    let tel = $("#tel").val()
    if (tel.length === 0) {
        $('#telRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // Country
    let country = $("#country").val()
    if (country.length === 0) {
        $('#countryRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // DoB
    let dob = $("#dob").val()
    if (dob.length === 0) {
        $('#dobRequired').removeClass('d-none')

        signInFormIsValid = false
    }

    // Member Organization
    let memberOrganization = $("#memberOrganization").val()


    $('#updateProfileButton').submit(function (e){
        if (!signInFormIsValid){
        e.preventDefault(); //prevents refresh or reload of form before validation

        }
    });
}

function resetJoinUsForm() {
    if (!$("#genderRequired").hasClass("d-none")) $("#genderRequired").addClass("d-none")
    if (!$("#streetAddressRequired").hasClass("d-none")) $("#streetAddressRequired").addClass("d-none")
    if (!$("#cityRequired").hasClass("d-none")) $("#cityRequired").addClass("d-none")
    if (!$("#cityDigit").hasClass("d-none")) $("#cityDigit").addClass("d-none")
    if (!$("#stateRequired").hasClass("d-none")) $("#stateRequired").addClass("d-none")
    if (!$("#zipCodeRequired").hasClass("d-none")) $("#zipCodeRequired").addClass("d-none")
    if (!$("#telRequired").hasClass("d-none")) $("#telRequired").addClass("d-none")
    if (!$("#countryRequired").hasClass("d-none")) $("#countryRequired").addClass("d-none")
    if (!$("#dobRequired").hasClass("d-none")) $("#dobRequired").addClass("d-none")
}