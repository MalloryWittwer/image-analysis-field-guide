function insertText(button) {
    var buttonText = button.textContent;
    var inputElement = document.querySelector('.dataTables_wrapper .dataTables_filter input');
    inputElement.value += ' ';
    inputElement.value += buttonText;
    inputElement.value += ' ';
    var event = new Event('input', { bubbles: true, cancelable: true });
    inputElement.dispatchEvent(event);
}