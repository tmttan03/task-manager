$( document ).ready(function() {

    $( "a[id^='openPublishBtn']" ).each(function( index ) {
        var url = $(this).data('action');
        $(this).click( function() {
            $('#publishDraft').attr('action', '');
            $('#publishDraft').attr('action', url);
        });  
    });

    $( "a[id^='openArchiveBtn']" ).each(function( index ) {
        var url = $(this).data('action');
        $(this).click( function() {
            $('#archiveDraft').attr('action', '');
            $('#archiveDraft').attr('action', url);
        });  
    });


    $( "a[id^='openDeleteBtn']" ).each(function( index ) {
        var url = $(this).data('action');
        $(this).click( function() {
            $('#deleteDraft').attr('action', '');
            $('#deleteDraft').attr('action', url);
        });  
    });

})

function updateTask(checkbox, id) {
    const formName = 'task-form-' + id;
    const form = document.getElementById(formName);
    const completedCheckbox = checkbox;
    const csrfToken = $('input[name="csrfmiddlewaretoken"]', form).val();  // Assuming the name is "csrftoken"

    console.log(formName);
    // Create a FormData object to hold form data
    const formData = new FormData(form);
    formData.append('completed', completedCheckbox.checked);  // Use .checked for boolean value

    // Send an AJAX request to the update-task-complete route
    fetch(form.action, {
      method: 'POST',
      body: formData,  // Send data using FormData
      headers: {
        'X-CSRFToken': csrfToken
      }
    })
    .then(response => response.json())
    .then(data => {
      // Handle successful update (optional: display confirmation message)
      console.log('Task updated successfully:', data);
      window.location.reload();
    })
    .catch(error => {
      console.error('Error updating task:', error);
    });
}





