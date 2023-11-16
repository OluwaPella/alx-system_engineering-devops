# Manage the contents of the /etc/default/nginx file
file { '/etc/default/nginx':
  ensure  => file,
  content => template('your_module/nginx_default.erb'), # Use a template or specify the content directly
  notify  => Exec['nginx-restart'], # Notify the restart exec when the file changes
}

# Restart Nginx when the /etc/default/nginx file changes
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/local/bin/:/bin/',
  refreshonly => true, # Only run when notified
}
