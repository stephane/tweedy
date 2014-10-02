var gulp = require('gulp');

var bowerFiles = require('main-bower-files');
var concat = require('gulp-concat');
var filter = require('gulp-filter');
var flatten = require('gulp-flatten');
var uglify = require('gulp-uglify');
var minifyCss = require('gulp-minify-css');
var streamqueue = require('streamqueue');
var livereload = require('gulp-livereload');

/* Build JS */
gulp.task('js', function() {
  var jsFilter= filter('**/*.js');
  return gulp.src(bowerFiles())
    .pipe(jsFilter)
    .pipe(uglify())
    .pipe(concat('base.min.js'))
    .pipe(gulp.dest('tweedy/static/build/js'));
});

/* Concat CSS */
gulp.task('css', function() {
  var cssFilter = filter('**/*.css');
  return gulp.src(bowerFiles())
    .pipe(cssFilter)
    .pipe(minifyCss())
    .pipe(concat('base.min.css'))
    .pipe(gulp.dest('tweedy/static/build/css'));
});

/* Bootstrap fonts */
gulp.task('fonts', function() {
  var fontsFilter = filter('**/fonts/*');
  return gulp.src(bowerFiles())
    .pipe(fontsFilter)
    .pipe(flatten())
    .pipe(gulp.dest('tweedy/static/build/fonts'));
});

gulp.task('watch', function() {
  var server = livereload();
  gulp.watch(['tweedy/**/*.html', 'tweedy/**/*.css', 'tweedy/**/*.js']).on('change', function(file) {
    server.changed(file.path);
  });
});


/* To check list of main files (Bower) */
gulp.task('bower-ls', function() {
  return gulp.src(bowerFiles())
    .pipe(gulp.dest('bower_ls'));
});

gulp.task('default', ['js', 'css', 'fonts']);
