.then(function (response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }
    response.json().then(function (data) {
      console.log(data);
    });
  })
  .catch(function (error) {
    console.log("Fetch error: " + error);
  });