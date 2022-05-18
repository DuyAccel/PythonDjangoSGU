
$(document).ready(function() {

    window.onload = function(){
        
    }
    /* =============================== Loading Animate =============================== */ 
    $('.Account__Register__Right__Loading, .Account__Register__Right__Alert__Success, .Account__Register__Right__Error').hide()



    function checkEmpty (str) {
        if (str.trim().length > 4) {
            return true
        }
        return false
    }

    function checkEmail (email) {
        email = email.trim()
        const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
        return emailRegex.test(email)
    }

    function checkUsername (username) {
        username = username.trim()
        const usernameRegex = /^[a-z0-9_.]+$/
        return usernameRegex.test(username)
    }

    function checkPassword (password) {
        password = password.trim()
        const passwordRegex = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[a-zA-Z!#$@^%&? "])[a-zA-Z0-9!#$@^%&?]{8,20}$/
        return passwordRegex.test(password)
    }

    function checkCFPassword (cfpassword, password) {
        cfpassword = cfpassword.trim()
        password = password.trim()
        if (cfpassword === password) {
            return true
        } else {
            return false
        }
    }

    $('.Account__Register__Right__Input__Item input').map (function() {
        $(this).blur(function() {
            if (!checkEmpty($(this).val())) {
                $(this).parent().children(2).show()
            }
        })
    })

    function notifyError (elmError, condition) {
        condition ? elmError.hide() : elmError.show()
    }

    $('#inputUsername').keyup(function() {
        notifyError ($('.Account__Register__Right__Error__Username'), checkUsername($(this).val()))
    })
    
    $('#inputEmail').keyup(function() {
        notifyError ($('.Account__Register__Right__Error__Email'), checkEmail($(this).val()))
    })

    $('#inputPassword').keyup(function() {
        notifyError ($('.Account__Register__Right__Error__Password'), checkPassword($(this).val()))
    })

    $('#inputCFPassword').keyup(function() {
        notifyError ($('.Account__Register__Right__Error__CFPassword'), checkCFPassword($(this).val(), $('#inputPassword').val()))
    })

    $('#SubmitSignUp').click(function () {
        document.getElementById("FormSignUp").submit()
    })

})
