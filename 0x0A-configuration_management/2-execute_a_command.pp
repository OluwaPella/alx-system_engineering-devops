# This script kill the process called killmenow
exec { 'kill':
  command     => 'pkill -f killmenow'
  path        => ['/usr/bin', '/usr/sbin']
}
