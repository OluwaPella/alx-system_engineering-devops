#!/usr/bin/env bash
# this script install using puppet
file {' ~/.ssh/id_rsa':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600';
