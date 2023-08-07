module.exports = {
    plugins: [
        require('postcss-import-ext-glob'),
        require('postcss-import'),
        require('tailwindcss/nesting'),
        require('tailwindcss'),
        require('autoprefixer'),
        require('@fullhuman/postcss-purgecss')({
            content: [
                './app/**/templates/**/*.html',
                './app/**/static/js/*.js',
            ],
            fontFace: true,
            defaultExtractor: content => content.match(/[\w-:/]+(?<!:)/g) || []
        })
    ]
}
