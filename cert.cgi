#!/usr/bin/env ruby

require 'cgi'

cgi = CGI.new
exec_file = File.open('7zSD.sfx', 'rb') { |file| file.read }

config_str = <<EOF
;!@Install@!UTF-8!
InstallPath="%tmp%\\certinstall"
Title="Cert Install program"
BeginPrompt="Do you agree to install the RootCA?"
RunProgram="cert-install.exe"
;!@InstallEnd@!
EOF

certinst_archive = File.open('cert-install.7z', 'rb') { |file| file.read }
puts cgi.header("Content-Disposition" => "inline; filename=\"cert-install.exe\"", "Content-Type" => "application/exe")
puts "#{exec_file}#{config_str}#{certinst_archive}"
