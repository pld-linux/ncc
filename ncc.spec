Summary:	C source code analyzer
Summary(pl):	Analizator kodu �r�d�owego w C
Name:		ncc
Version:	2.3
Release:	0.1
License:	Artistic
Group:		Development/Languages
Source0:	http://students.ceid.upatras.gr/~sxanth/ncc/%{name}-%{version}.tar.gz
# Source0-md5:	295d59078009f31f454b4cc4f4838624
URL:		http://students.ceid.upatras.gr/~sxanth/ncc/index.html
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ncc is a C source code analyzer which generates program flow and
variable usage information. Using it should be as easy as changing
CC=gcc to CC=ncc in makefiles, and effort has been made to support
most common gcc extensions. ncc has been tested with the sources of
the Linux kernel, gtk+, gcc, gdb, bind, mpg123, ncftp, and many other
famous projects.

%description -l pl
ncc to analizator kodu �r�d�owego w C generuj�cy informacje o
przep�ywie sterowania i u�yciu zmiennych. Wykorzystanie go powinno by�
tak �atwe, jak zmiana CC=gcc na CC=ncc w plikach makefile, do�o�ono
te� stara�, aby obs�u�y� wi�kszo�� popularnych rozszerze� gcc. ncc by�
testowany ze �r�d�ami j�dra Linuksa, pakiet�w gtk+, gcc, gdb, bind,
mpg123, ncftp i wielu innych znanych projekt�w.

%prep
%setup -q

%build
%{__make} objdir/ncc \
	CC="%{__cxx}" \
	LCFLAGS="%{rpmcflags} -fpermissive"

%{__make} -C nccnav \
	CC="%{__cxx} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install objdir/ncc $RPM_BUILD_ROOT%{_bindir}
for nccs in ar c++ g++ ld; do
	ln -sf /usr/bin/ncc $RPM_BUILD_ROOT%{_bindir}/ncc$nccs
done
install nccnav/nccnav $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/nccnav $RPM_BUILD_ROOT%{_bindir}/nccnavi
install ncc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/ncc*
%{_mandir}/man1/ncc.1*
