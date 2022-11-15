const makeJson = json => {
   json = json.replace('[', '');
   json = json.replace(']', '');
   json = json.replaceAll("'", '"');
   json = json.replaceAll(' ', '');
   json = json.replace(/\r/gi, '\\r').replace(/\n/gi, '\\n');
   json = json.replace('"', '');
   json = json.replace('"]', ']');
   return json;
};

export const handleMohoRouter = (req, res) => {
   const pythonShell = require('python-shell');
   const options = {
      mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
   };

   pythonShell.PythonShell.run('moho.py', options, (error, results) => {
      let json = JSON.stringify(results);
      json = makeJson(json);
      res.json(json);
      return res.end();
   });
};

export const handleMyOwnHomeRouter = (req, res) => {
   const pythonShell = require('python-shell');
   const options = {
      mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
   };

   pythonShell.PythonShell.run('myownhome.py', options, (error, results) => {
      let json = JSON.stringify(results);
      json = makeJson(json);
      res.json(json);
      return res.end();
   });
};
