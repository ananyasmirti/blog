tinymce.init({
    selector: 'textarea',
    plugins: 'code autosave autoresize image fullscreen fullpage imagetools table wordcount link paste textcolor textpattern',
    toolbar: 'a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table',
    toolbar_mode: 'floating',
    mode : "textareas",
    force_br_newlines : false,
    force_p_newlines : false,
    forced_root_block : '',
    setup: function (editor) {
        editor.on('change', function () {
            editor.save();
        });
        
    }
    

  });