var uppy = Uppy.Core()
.use(Uppy.Dashboard, {
    inline: true,
    target: '#drag-drop-area',
    showProgressDetails: true,
    metaFields: [
        { id: 'name', name: 'Name', placeholder: 'file name' },
        { id: 'caption', name: 'Caption', placeholder: 'describe what the image is about' }
    ],
})
.use(
    Uppy.AwsS3Multipart,
    {
        companionUrl: '/uppy/',
    }
)

uppy.on('complete', (result) => {
    console.log('Upload complete! We’ve uploaded these files:', result.successful)
});