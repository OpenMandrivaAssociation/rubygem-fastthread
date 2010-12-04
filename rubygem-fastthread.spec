%define	oname	fastthread

Summary:	Optimized replacement for thread.rb primitives
Name:		rubygem-%{oname}
Version:	1.0.7
Release:	%mkrel 2
License:	GPLv2+ or Ruby License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-devel ruby-RubyGems
Requires:	ruby
Provides:	rubygem(%{oname}) = %{version}

%description
Optimized replacement for thread.rb primitives.

%prep

%build
mkdir -p .{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} --force %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -rf .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}

#install arch dependant files in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/%{oname}.so
