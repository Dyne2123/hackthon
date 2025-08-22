import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import { useState, useRef, useEffect } from 'react';
import { getEditorContent } from '../api';

export default function Validator() {
  const [content, setContent] = useState('');
  const [copiedText, setCopiedText] = useState([]);
  const quillRef = useRef();

 
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getEditorContent();
        setContent(response.content);
        setCopiedText(response.pasted_text || []);
        console.log("Pasted text array:", response.pasted_text);
      } catch (err) {
        console.error("Error fetching editor content:", err);
      }
    };
    fetchData();
  }, []);

 
  useEffect(() => {
    if (!content || !copiedText.length || !quillRef.current) return;

    const quill = quillRef.current.getEditor();
    const text = quill.getText();

    copiedText.forEach((phrase) => {
      if (!phrase) return;
      const escaped = phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); 
      const regex = new RegExp(escaped, 'gi'); 
      let match;

      while ((match = regex.exec(text)) !== null) {
        quill.formatText(match.index, phrase.length, { bold: true, color: 'red' });
      }
    });
  }, [content, copiedText]);

  return (
    <ReactQuill
      ref={quillRef}
      theme="snow"
      value={content}
      readOnly={true}
    />
  );
}
