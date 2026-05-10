/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Permet les appels API vers le backend Django en développement
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://backend:8000/api/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
