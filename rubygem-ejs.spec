#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ejs
Version  : 1.1.1
Release  : 3
URL      : https://rubygems.org/downloads/ejs-1.1.1.gem
Source0  : https://rubygems.org/downloads/ejs-1.1.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
EJS (Embedded JavaScript) template compiler for Ruby
====================================================

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ejs-1.1.1
gem spec %{SOURCE0} -l --ruby > rubygem-ejs.gemspec

%build
gem build rubygem-ejs.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
ejs-1.1.1.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ejs-1.1.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/cdesc-EJS.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/compile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/escape_function-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/escape_pattern-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/evaluate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/evaluation_pattern-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/interpolation_pattern-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/js_escape%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/js_unescape%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/replace_escape_tags%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/replace_evaluation_tags%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/EJS/replace_interpolation_tags%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ejs-1.1.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/ejs-1.1.1/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/ejs-1.1.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/ejs-1.1.1/lib/ejs.rb
/usr/lib64/ruby/gems/2.2.0/specifications/ejs-1.1.1.gemspec
