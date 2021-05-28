/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    alert("Yoo")
    evt.preventDefault()

    const name = $("#name").val();
    const email = $("#email").val();
    const year = $("#year").val();
    const color = $("#color").val();
    console.log(email)
    const res = await axios.post(`/api/get-lucky-num`, {
      name, email, year, color
    });
    // console.log(res)
    handleResponse(res)
  }
/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    // console.log(resp)
    if (resp.data.error) {
        for (let err in resp.data.error) {
            $(`#${err}-err`).append(`<p>${resp.data.error[err]}</p>`)
        }
    }
    else {
        $("#lucky-results").append(`<p>Your lucky number is ${resp.data.num.num} (${resp.data.num.fact})</p>`)
        $("#lucky-results").append(`<p>Your birth year is ${resp.data.year.year} (${resp.data.year.fact})</p>`)
    }
}


$("#lucky-form").on("submit", processForm);
