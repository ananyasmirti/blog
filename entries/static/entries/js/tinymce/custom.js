tinymce.init({
    selector: 'textarea',
    plugin: 'fullscreen fullpage link',
    setup: function (editor) {
        editor.on('change', function () {
            tinymce.triggerSave();
        });
    }
  });