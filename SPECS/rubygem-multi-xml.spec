# Generated from multi_xml-0.5.5.gem by gem2rpm -*- rpm-spec -*-
%global gemname multi_xml

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A generic swappable back-end for XML parsing
Name: rubygem-%{gemname}
Version: 0.5.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/sferik/multi_xml
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.5
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) >= 1.3.5
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Provides swappable XML backends utilizing LibXML, Nokogiri, Ox, or REXML.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Aug 14 2013  <bradejr@puppetlabs.com> - 0.5.5-1
- Initial package
