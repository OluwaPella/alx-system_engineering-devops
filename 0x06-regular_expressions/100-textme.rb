#!/usr/bin/env ruby
# A regular expression that reponds and give details
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
