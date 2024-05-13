# Set open file limit higher

# Update the file limit in the /etc/default/nginx file
exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}

# Restart the nginx service to apply the changes
exec { 'reboot nginx':
  command => '/usr/sbin/service nginx restart'
}