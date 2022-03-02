async function load_laptops_data() {
    var requestOptions = {
      method: 'GET',
    };

    fetch("http://127.0.0.1:8000/api/v1/stats/cheapest_laptops_best_reviews")
        .then(response =>
        {
            if (!response.ok)
            {
                throw new Error('Network response was not OK');
            }
            return response.json()
        })
        .then(jsonContent =>
        {
            console.log(jsonContent)
            document.getElementById("best_5_laptops").innerHTML = JSON.stringify(jsonContent)
        })
        .catch(error => console.log('error', error));
}
