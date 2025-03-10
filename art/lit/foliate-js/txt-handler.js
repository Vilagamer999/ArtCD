// text-handler.js
class TextBook {
    constructor(file) {
        this.file = file;
        this.sections = [{
            load: async () => {
                const text = await file.text();
                const blob = new Blob([`
                    <html>
                        <head>
                            <style>
                                body {
                                    margin: 2em;
                                    line-height: 1.6;
                                    font-family: system-ui, -apple-system, sans-serif;
                                }
                                p { margin: 1em 0; }
                            </style>
                        </head>
                        <body>
                            <pre style="white-space: pre-wrap;">${text}</pre>
                        </body>
                    </html>
                `], { type: 'text/html' });
                return URL.createObjectURL(blob);
            },
            size: file.size
        }];
        this.metadata = {
            title: file.name,
            author: 'Unknown',
            language: 'en'
        };
    }
}
