// src/components/SearchBar.js
import React from 'react';

const SearchBar = ({ onSearch }) => {
  return (
    <div className="flex gap-2">
      <input type="text" placeholder="Search recipes..." className="border border-gray-300 rounded-md shadow-sm p-2" />
      {/* Add filters for dietary preferences */}
      <button onClick={onSearch} className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
        Search
      </button>
    </div>
  );
};

export default SearchBar;
