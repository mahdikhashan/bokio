var quill = new Quill('#quill-container', {
  modules: {
    toolbar: [
      [{ header: [1, 2, 3, false] }],
      ['bold', 'italic', 'underline'],
      ['image', 'code-block']
    ]
  },
  scrollingContainer: '#scrolling-container', 
  placeholder: 'بنویسید تا بمانید...',
  theme: 'bubble'
});
