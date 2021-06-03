<?php 

if(class_exists('Phar')){

     $phar = new Phar('blog.phar',0,'blog.phar');

     $phar ->buildFromDirectory(__DIR__.'/blog');

     $phar->setStub($phar->createDefaultStub('index.php'));
     $phar-> compressFiles(Phar::GZ);
}