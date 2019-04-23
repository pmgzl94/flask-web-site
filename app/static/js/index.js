function validatepsswd() {
    var a = document.forms["register_form"]["user_password"].value;
    var b =  document.forms["register_form"]["user_password_confirm"].value;
    if (a != b) {
        alert("Please enter the same password !!");
        document.register_form.user_password_confirm.focus();
        return false;
    }
    return true;
}
