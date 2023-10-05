#!/usr/bin/bash
# this explain how to use puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites_enabled/default',
  after  =>  'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/ permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello Word!',
}

server { 'nginx':
  ensure  => running,
  require => package['nginx'],
}
