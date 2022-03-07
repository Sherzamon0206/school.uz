
function share_data(){
        name = document.getElementById('name').value
        email = document.getElementById('email').value
        message= document.getElementById(`message`).value

        if(name==""|| email==""||message==""){
            document.getElementById('text').innerHTML = `Barcha formalarni to'ldirganingizga ishonch hosil qiling`

        }
        else {
                    var url = `/contact/`
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'name': name,


                    'email': email,

                    'message': message,

                })
                })
                .then((response) => {
                    response.json().then((data) => {
                        data = data['data']
                    })
                })

            document.getElementById('saqla2').innerHTML = `
              ${name} !   Siz bilan tez orada bog'lanamiz,Fikringiz uchun rahmat!!! 
       
                `
                }



           }


