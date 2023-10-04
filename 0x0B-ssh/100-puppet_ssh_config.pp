#!/usr/bin/env bash
# this script install using puppet
file { '~/.ssh/id_rsa':
  ensure => present
