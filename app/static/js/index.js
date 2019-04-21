
function validate() {
    if (document.register_form.user_password !=
        document.register_form.user_password_confirm) {
        alert("Please enter the same password !!");
        document.register_form.user_password_confirm.focus();
        return false;
    }
    return true;
}
