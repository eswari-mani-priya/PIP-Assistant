window.onload = function () {
    var app = new Vue({
        delimiters: ['[[',']]'],
        el: '#app',
        data: {
            messages: [],
            input: '',
            send_blank: false,
            placeholder: 'Ask PIP about Python....',
        },
        created: function(){

        },
        methods: {
        add_message: function() {
            if(this.input.length > 0) {
                var message = {
                    'text': this.input,
                    'user': true,
                    'chat_bot': false,
                };
                this.messages.push(message);
                this.input = '';
                this.send_blank = false;
                this.placeholder = 'Ask PIP about Python....';
                fetch("/pip/get-response/", {
                body: JSON.stringify({'message': message['text']}),
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'content-type': 'application/json'
                },
                method: 'POST',
                mode: 'cors',
                redirect: 'follow',
                referrer: 'no-referrer',
                })
                .then(response => response.json()).then((json) => {
                    this.messages.push(json['message'])
                })
            } else{
                this.send_blank = true;
                this.placeholder = 'Please put in some text';
            }

        },
        check_content: function(){
            if(this.input.length > 0){
                this.send_blank = false;
                this.placeholder = 'Ask PIP about Python....';
            } else {
                this.send_blank = true;
                this.placeholder = 'Please put in some text';
            }
        },

    }
  });
};