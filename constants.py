MAIN_PAGE_URL = 'https://stellarburgers.education-services.ru'

DRAG_AND_DROP_SCRIPT = """
    var source = arguments[0];
    var target = arguments[1];

    function fire(el, type) {
        var evt = new DragEvent(type, { bubbles: true, cancelable: true });
        el.dispatchEvent(evt);
    }

    fire(source, 'dragstart');
    fire(target, 'dragenter');
    fire(target, 'dragover');
    fire(target, 'drop');
    fire(source, 'dragend');
"""