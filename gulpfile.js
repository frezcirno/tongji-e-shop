const gulp = require('gulp'),
    // connect = require('gulp-connect'),
    // uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch'),
    fileinclude = require('gulp-file-include');

gulp.task('webserver', function () {
    connect.server({
        root: 'dist',
        livereload: true,
        port: 2333
    });
});

gulp.task('html', function () {
    return gulp.src('src/html/*.html')
        .pipe(fileinclude({
            prefix: '@@',  // 自定义标识前缀
            basepath: 'src/html/components'  // 复用组件目录
        }))
        .pipe(gulp.dest('templates')) // 生成静态文件
        // .pipe(connect.reload());    // 刷新浏览器
})

gulp.task('js', function () {
    return gulp.src('src/js/*.js')
        // .pipe(uglify())
        .pipe(gulp.dest('static/js'))
        // .pipe(connect.reload());
});

gulp.task('sass', function () {
    return gulp.src('src/css/*.scss')
        .pipe(fileinclude({
            prefix: '//@@',  // 自定义标识前缀
            basepath: 'src/css/components'  // 复用组件目录
        }))
        .pipe(sass({ outputStyle: 'expanded' }))
        .on('error', function (err) {
            console.error('sassError!', err.message);
        })
        .pipe(gulp.dest('static/css'))
        // .pipe(connect.reload());
});

gulp.task('watch', function () {
    watch('src/js/**/*.js', gulp.series('js'));
    watch('src/css/**/*.scss', gulp.series('sass'));
    watch('src/html/**/*.html', gulp.series('html'));
});

gulp.task('default', gulp.parallel('watch'));
