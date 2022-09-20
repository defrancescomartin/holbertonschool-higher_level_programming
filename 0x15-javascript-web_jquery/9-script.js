$.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET'
  })
    .done(function (response) {
      $('DIV#hello').text(response.hello);
    });
