%define	oname	fastthread

Summary:	Optimized replacement for thread.rb primitives
Name:		rubygem-%{oname}
Version:	1.0.7
Release:	3
License:	GPLv2+ or Ruby License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRequires:	ruby-devel ruby-RubyGems
Requires:	ruby
Provides:	rubygem(%{oname}) = %{version}

%description
Optimized replacement for thread.rb primitives.

%prep

%build
mkdir -p %buildroot/%{ruby_gemdir}

%install
gem install -V --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
