// static/js/script.js

var itemToDelete;
var urlToDelete;

function confirmDelete(item, url) {
    itemToDelete = item;
    urlToDelete = url;
    document.getElementById('deleteModal').style.display = 'block';
}

function deleteItem() {
    if (itemToDelete) {
        fetch(urlToDelete + itemToDelete + '/')
            .then(response => {
                if (response.ok) {
                    //alert('Elemento ' + itemToDelete + ' eliminado.');
                    // Puedes actualizar la página o realizar alguna otra acción después de la eliminación
                    location.reload();
                } else {
                    alert('Error al eliminar el elemento.');
                }
                // Ocultar el modal después de la confirmación
                document.getElementById('deleteModal').style.display = 'none';
            })
            .catch(error => {
                console.error('Error al eliminar el elemento:', error);
                alert('Error al eliminar el elemento.');
                // Ocultar el modal después de la confirmación
                document.getElementById('deleteModal').style.display = 'none';
            });
    } else {
        console.error('Error: itemToDelete no tiene un valor válido.');
        alert('Error al eliminar el elemento.');
        // Ocultar el modal después de la confirmación
        document.getElementById('deleteModal').style.display = 'none';
    }
}

function cancelDelete() {
    // Cancelar la eliminación, simplemente ocultar el modal
    document.getElementById('deleteModal').style.display = 'none';
}
