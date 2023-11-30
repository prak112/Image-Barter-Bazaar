// detect events on add-to-cart button
document.querySelector('#add-to-cart').addEventListener('click', function() {
    //notification banner
    displayNotificationBanner();
    window.location.href = '/photostore/products';
    
    // AJAX request to add_to_cart
    // var request = new XMLHttpRequest();
    // request.open('GET', '/photostore/add_to_cart/', true);
    // request.onreadystatechange = function() {
    //     if (request.readyState === XMLHttpRequest.DONE && request.status === 200){
    //         // update DOM based on view 'add_to_cart' response
    //         var response = JSON.parse(request.responseText);
    //         if (response.success){
    //             // notification banner
    //             displayNotificationBanner();
    //             window.location.href = '/photostore/products';
    //         }
    //     }
    // };
    // request.send();
});

function displayNotificationBanner() {
    document.querySelector('.notification').style.display = 'block';
    setTimeout(function() {
        document.querySelector('.notification').style.display = 'none';
    }, 2000);
}