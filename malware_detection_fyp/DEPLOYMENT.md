# CyberShield AI Deployment Guide

## Quick Deployment Options

### Option 1: Render (Recommended)
1. Connect your GitHub repo to Render
2. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn cyber_deploy:app --bind 0.0.0.0:$PORT`
   - **Environment**: Python 3.9.18

### Option 2: Railway
1. Connect GitHub repo to Railway
2. Railway will auto-detect the Python app
3. No additional configuration needed

### Option 3: Heroku
1. Install Heroku CLI
2. Run these commands:
```bash
heroku create your-app-name
git push heroku main
```

## Pre-Deployment Checklist

1. **Check Dependencies**:
   ```bash
   python check_deployment.py
   ```

2. **Ensure Model Files Exist**:
   - Make sure `models/` directory contains `.keras` files
   - Run `python train_model.py` if no models exist

3. **Test Locally**:
   ```bash
   python cyber_deploy.py
   ```

## Environment Variables

- `PORT`: Server port (auto-set by most platforms)
- `FLASK_ENV`: Set to 'production' for production deployment

## File Structure Required for Deployment

```
malware_detection_fyp/
├── cyber_deploy.py          # Main application
├── app.py                   # Alternative entry point
├── requirements.txt         # Dependencies
├── Procfile                 # Heroku process file
├── runtime.txt              # Python version
├── render.yaml              # Render configuration
├── models/                  # Trained model files
│   └── *.keras
├── src/                     # Source code
│   ├── predictor.py
│   ├── model_builder.py
│   └── data_loader.py
└── temp_uploads/            # Upload directory (auto-created)
```

## Troubleshooting

### TensorFlow Issues
- Using `tensorflow-cpu` for better compatibility
- Version range: 2.13.0 to 2.16.0

### Memory Issues
- Model uses 128x128 images to reduce memory usage
- Batch processing for predictions

### File Upload Issues
- Max file size: 16MB
- Supported formats: PNG, JPG, JPEG, BMP, TIFF

## Platform-Specific Notes

### Render
- Free tier has 512MB RAM limit
- Uses `render.yaml` configuration
- Automatic HTTPS

### Railway
- Generous free tier
- Auto-detects Python apps
- Built-in monitoring

### Heroku
- Uses `Procfile` for process definition
- Requires `runtime.txt` for Python version
- Ephemeral filesystem (uploads are temporary)

## Success Indicators

✅ Application starts without errors
✅ Model loads successfully
✅ Web interface is accessible
✅ File upload works
✅ Predictions are generated

## Support

If deployment fails:
1. Check the deployment logs
2. Verify all files are committed to git
3. Ensure model files are present
4. Run `python check_deployment.py` locally