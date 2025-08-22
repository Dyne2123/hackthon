import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import { useState, useRef, useEffect } from 'react';
import styles from './editor.module.css';
import { sendEditorContent } from '../api.jsx';

export default function Editor() {
  const [content, setContent] = useState('');
  const [pastedText, setPastedText] = useState([]); 
  const quillRef = useRef();

  const handleContentChange = (value) => {
    setContent(value);
  };

  const modules = {
    toolbar: [
      [{ 'font': [] }, { 'size': [] }],
      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      ['bold', 'italic', 'underline', 'strike'],
      [{ 'color': [] }, { 'background': [] }],
      [{ 'script': 'sub' }, { 'script': 'super' }],
      ['blockquote', 'code-block'],
      [{ 'list': 'ordered' }, { 'list': 'bullet' }, { 'indent': '-1' }, { 'indent': '+1' }],
      [{ 'direction': 'rtl' }, { 'align': [] }],
      ['image', 'formula'],
      ['clean']
    ]
  };

  const formats = [
    'header', 'font', 'size',
    'bold', 'italic', 'underline', 'strike',
    'color', 'background',
    'script',
    'blockquote', 'code-block',
    'list', 'bullet', 'indent',
    'image', 'formula',
    'align', 'direction',
    'clean'
  ];

  const handleSubmit = () => {
    sendEditorContent(content, pastedText);
  };

  useEffect(() => {
    if (!quillRef.current) return;
    const quill = quillRef.current.getEditor();

    //gets clipboard data
    const handlePaste = (e) => {
      const pasted = e.clipboardData.getData('text/plain').trim();
      if (!pasted) return;

      setPastedText((prev) => {
        const updated = [...prev, pasted];
        console.log("Pasted text array:", updated);
        return updated;
      });
    };

    //paste triggering event
    quill.root.addEventListener('paste', handlePaste);

    return () => {
      quill.root.removeEventListener('paste', handlePaste);
    };
  }, [content]);

  return (
    <div className={styles.outer}>
      <ReactQuill
        ref={quillRef}
        theme="snow"
        value={content}
        modules={modules}
        formats={formats}
        onChange={handleContentChange}
        className={styles.editor}
      />
      {/* <button onClick={handleSubmit}>Submit</button> */}
    </div>
  );
}
