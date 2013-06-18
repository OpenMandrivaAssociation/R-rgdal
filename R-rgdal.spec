%global packname  rgdal
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.8.5
Release:          2
Summary:          Bindings for the Geospatial Data Abstraction Library
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rgdal_0.8-5.tar.gz
Requires:         R-methods R-sp
Requires:         gdal
Requires:         gdal-devel
Requires:         proj
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-sp
BuildRequires:    gdal
BuildRequires:    gdal-devel
BuildRequires:    proj

%description
Provides bindings to Frank Warmerdam's Geospatial Data Abstraction Library
(GDAL) (>= 1.3.1) and access to projection/transformation operations from
the PROJ.4 library. The GDAL and PROJ.4 libraries are external to the
package, and, when installing the package from source, must be correctly
installed first. Both GDAL raster and OGR vector map data can be imported
into R, and GDAL raster data and OGR vector data exported. Use is made of
classes defined in the sp package. Windows binaries (including GDAL,
PROJ.4 and Expat) are provided on CRAN. Mac Intel OS X binaries (including
GDAL, PROJ.4 and Expat) are not provided on CRAN, but can be installed
from the CRAN Extras repository with: setRepositories(ind=1:2);

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README*
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/OSGeo4W_test
%{rlibdir}/%{packname}/SVN_VERSION
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/vectors
