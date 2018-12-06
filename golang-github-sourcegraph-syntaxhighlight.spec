# Run tests in check section
%bcond_without check

%global goipath         github.com/sourcegraph/syntaxhighlight
%global commit          bd320f5d308e1a3c4314c678d8227a0d72574ae7

%global common_description %{expand:
Syntaxhighlight provides syntax highlighting for code. It currently uses a 
language-independent lexer and performs decently on JavaScript, Java, Ruby, 
Python, Go, and C.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Syntax highlighting of code
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/sourcegraph/annotate)

%if %{with check}
BuildRequires: golang(github.com/kr/pretty)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build 
%gobuildroot
%gobuild -o _bin/syntaxhighlight %{goipath}/cmd/syntaxhighlight


%install
%goinstall
install -Dpm 0755 _bin/syntaxhighlight %{buildroot}%{_bindir}/syntaxhighlight


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE
%{_bindir}/syntaxhighlight


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitbd320f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418gitbd320f5
- First package for Fedora

