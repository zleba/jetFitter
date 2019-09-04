p=$PWD
mkdir xfitterBuild
cd xfitter-2.0.1

sed -i 's/-std=c++11/-std=c++17/' configure.ac

#libTool black magic
libtoolize
aclocal
autoreconf -i

./configure --prefix=$p/xfitterBuild  --enable-lhapdf --disable-applgrid
