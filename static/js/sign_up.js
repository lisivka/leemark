$(document).ready(() => {

    // alert("Hello, jQuery!");
    // example1();
    // example2();

    let correct1 = false;
    let correct2 = false;
    let correct3 = false;
    let correct4 = false;

    let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{4,15}$/; //   логин    /^$/ - стандарт с первого до последнего '\' екранирование
    let regExp2 = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-\$#&])[A-Za-z0-9_\-\$#&]{8,}$/  // пароль
    let regExp3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/  // почта
    // $("#login").click(function() {
        // alert("login blur - work");
    // );

    $("#pass_1").blur(() => {
        // alert("login blur - work");
        let passX = $("#pass_1").val();
        if (regExp2.test(passX)) {
            $("#pass1_mess").html("ОК");
            correct2 = true;
        } else {
            correct2 = false;
            $("#pass1_mess").html("Минимум 8 символов, хотя бы одна Большая буква, одна цифра и символ ( _ - $ # &)")

        }
        // Проверка на совпадение двух паролей
        let passY = $("#pass_2").val();

        if (passX == passY ) {
            $("#pass2_mess").html("ОК");
            correct3 = true;
        } else {
            correct3 = false;
            $("#pass2_mess").html("Пароли НЕ совпадают")

        }

    });



    $("#pass_2").blur(() => {
        // alert("login blur - work");
        let passX = $("#pass_1").val();
        let passY = $("#pass_2").val();

        if (passX == passY ) {
            $("#pass2_mess").html("ОК");
            correct3 = true;
        } else {
            correct3 = false;
            $("#pass2_mess").html("Пароли НЕ совпадают")

        }
     });

    $("#email").blur(() => {
        // alert("login blur - work");
        let email_ = $("#email").val();
        if (regExp3.test(email_)) {
            $("#email_mess").html("ОК");
            correct4 = true;
        } else {
            correct4 = false;
            $("#email_mess").html("Введите коректный email")

        }
    });


    $("#login").blur(function() {

       // let loginX = $(this).val();
        let loginX = $("#login").val();
        if (regExp1.test(loginX)) {
            // Проверка занятости логина
            $.ajax({
                    url: "/accounts/ajax_reg",
                    data: "login=" + loginX,
                    success: function (result) {
                        if (result.message == "занят") {
                            $("#login_mess").html("Логин занят");
                            correct1 = false;
                        } else {
                            $("#login_mess").html(result.message);
                            correct1 = true;
                        }
                    }
            });

            correct1 = true;
            $("#login_mess").html("")
        } else {
            correct1 = false;
            $("#login_mess").html("Логин не соответсвует шаблону a-z A-Z 0-9 от 4 символов")
        }

    });


    $("#submit").click(() => {
        if (correct1 == true && correct2 == true && correct3 == true && correct4 == true) {
            $("#form1").attr("onsubmit", "return true");
        } else {
            $("#form1").attr("onsubmit", "return false");
            alert("Форма содержит не коректные данные!! \nОтправка данных заблокирована!");
        }
    });
});

