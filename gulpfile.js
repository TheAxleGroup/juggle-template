const {src, dest, watch, series} = require('gulp');
const browserSync = require('browser-sync');
const postcss = require('gulp-postcss');
const rename = require('gulp-rename');
const sourcemaps = require('gulp-sourcemaps');
const cleanCSS = require('gulp-clean-css');

const pimportGlob = require('postcss-import-ext-glob');
const pimport =  require('postcss-import');
const pnesting = require('tailwindcss/nesting');
const ptailwind = require('tailwindcss');
const pautoprefixer = require('autoprefixer');
const concat = require('gulp-concat');
const gzip = require('gulp-gzip');

const purge = postcss([
    require('@fullhuman/postcss-purgecss')({
        content: [
            './app/**/*.html',
            './app/**/*.js',
            './app/**/*.py',
        ],
        defaultExtractor: content => content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || [],

        safelist: {
            greedy: [/form/, /label/, /input/, /type/]
        }
    }),
]);

const prefix = postcss([pautoprefixer])

function tailwindTask() {
    process.env.NODE_ENV = 'development';
    return src('./app/**/*.pcss')
        .pipe(postcss([
                pimportGlob,
                pimport,
                pnesting,
                ptailwind
            ]
        ))
        .pipe(rename("style.tailwind.css"))
        .pipe(dest('./app/app/static/css/'));
}

function styleTask() {
    return src(['./app/**/fontawesome.all.css', './app/**/style.tailwind.css'])
        .pipe(concat('style.css'))
        .pipe(dest('./app/app/static/css/'))
}

function styleMinTask() {
    return src(['./app/**/fontawesome.all.css', './app/**/style.tailwind.css'])
        .pipe(concat('style.min.css'))
        .pipe(dest('./app/app/static/css/'))
}

function purgeFontawesomeTask() {
    return src('./app/app/static/css/fontawesome.all.css')
        .pipe(purge)
        .pipe(rename("fontawesome.purge.css"))
        .pipe(dest('./app/app/static/css/'))
}

function buildPurgeStyle() {
    return src(['./app/**/fontawesome.purge.css', './app/**/style.tailwind.css'])
        .pipe(concat("style.purge.css"))
        .pipe(dest('./app/app/static/css/'))
}

function buildMinTask() {
    return src('./app/app/static/css/style.purge.css')
        .pipe(sourcemaps.init())
        .pipe(prefix)
        .pipe(cleanCSS())
        .pipe(rename("style.min.css"))
        .pipe(sourcemaps.write('.'))
        .pipe(dest('./app/app/static/css/'));
}

function gzipCss() {
    return src('./app/app/static/css/style.css')
        .pipe(gzip({ append: false }))
        .pipe(dest('../css_gzip/'));
}

function gzipMinCss() {
    return src('./app/app/static/css/style.min.css')
        .pipe(gzip({ append: false }))
        .pipe(dest('../css_gzip/'));
}

function reloadTask(cb) {
    browserSync.reload();
    cb();
}

function serveTask(cb) {
    process.env.NODE_ENV = 'development';
    browserSync.init({
        proxy: "localhost:8000",
        notify: false,
        open: false,
    });
    cb();
}

// Watch Task
function watchTask() {
    watch(['./**/*.{html,py,js,pcss}'], series(tailwindTask, styleTask, styleMinTask, reloadTask));
}

exports.default = series(
    serveTask,
    tailwindTask,
    styleTask,
    styleMinTask,
    watchTask
);

exports.help = series(tailwindTask);

exports.build = series(tailwindTask, styleTask, purgeFontawesomeTask, buildPurgeStyle, buildMinTask, gzipCss, gzipMinCss);
