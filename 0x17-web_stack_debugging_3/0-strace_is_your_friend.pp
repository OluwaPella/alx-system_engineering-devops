# fixing bad file naming instead of php it was phpp that why Apache is returning a 500 error

exec{'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
