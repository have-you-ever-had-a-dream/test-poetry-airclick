#!/usr/bin/env python3
"""
Sample application for testing transitive reachability analysis.
Uses packages that may transitively depend on redshift-connector.
"""

import boto3
import requests

def use_boto3():
    """
    Use boto3 which may have redshift-connector as a transitive dependency.
    """
    try:
        # Create a boto3 session
        session = boto3.Session()
        print(f"Created boto3 session: {session}")
        
        # Create redshift client (may use redshift-connector internally)
        redshift = session.client('redshift', region_name='us-east-1')
        print(f"Created redshift client: {redshift}")
        
    except Exception as e:
        print(f"Error using boto3: {e}")

def use_coolpandas():
    """
    Use coolpandas which may have redshift-connector as a transitive dependency.
    """
    try:
        import coolpandas as cp
        print("coolpandas imported successfully")
        
        # Basic coolpandas usage
        df = cp.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print(f"Created coolpandas DataFrame: {df}")
        
    except ImportError as e:
        print(f"Could not import coolpandas: {e}")
    except Exception as e:
        print(f"Error using coolpandas: {e}")

def use_requests():
    """
    Use requests for HTTP operations.
    """
    try:
        print(f"requests version: {requests.__version__}")
        
        # Example usage that might trigger redshift connections
        response = requests.get("https://httpbin.org/json")
        print(f"HTTP request status: {response.status_code}")
        
    except Exception as e:
        print(f"Error using requests: {e}")

def test_vulnerable_dependencies():
    """
    Test code that uses packages with known vulnerabilities.
    This tests whether transitive dependencies are properly analyzed.
    """
    try:
        # Test Flask (has vulnerabilities in older versions)
        import flask
        print(f"Flask version: {flask.__version__}")
        
        # Test Jinja2 (has vulnerabilities in older versions)
        import jinja2
        print(f"Jinja2 version: {jinja2.__version__}")
        
        # Test PyYAML (has vulnerabilities in older versions)
        import yaml
        print(f"PyYAML version: {yaml.__version__}")
        
        # Test urllib3 (has vulnerabilities in older versions)
        import urllib3
        print(f"urllib3 version: {urllib3.__version__}")
        
        # Test cryptography (has vulnerabilities in older versions)
        import cryptography
        print(f"cryptography version: {cryptography.__version__}")
        
        # Test Pillow (has vulnerabilities in older versions)
        import PIL
        print(f"Pillow version: {PIL.__version__}")
        
        # Test Django (has vulnerabilities in older versions)
        import django
        print(f"Django version: {django.__version__}")
        
    except ImportError as e:
        print(f"Import error: {e}")
    except Exception as e:
        print(f"Error testing vulnerable dependencies: {e}")

def potentially_vulnerable_code():
    """
    Code that might use the vulnerable redshift-connector pattern.
    This tests whether transitive dependencies are properly analyzed.
    """
    try:
        # Check if redshift_connector is available transitively
        import redshift_connector
        print("redshift_connector found as transitive dependency")
        
        # Use the potentially vulnerable pattern
        connection = redshift_connector.connect(
            host="test-redshift-cluster.amazonaws.com",
            database="testdb", 
            user="testuser",
            auth_method="BrowserAzureOAuth2CredentialsProvider",
            port=5439
        )
        print(f"Redshift connection established: {connection}")
        
    except ImportError:
        print("redshift_connector not available as transitive dependency")
    except Exception as e:
        print(f"Error with redshift connection: {e}")

def main():
    print("Starting transitive reachability test...")
    print("=" * 50)
    
    use_boto3()
    print("-" * 30)
    
    use_coolpandas() 
    print("-" * 30)
    
    use_requests()
    print("-" * 30)
    
    test_vulnerable_dependencies()
    print("-" * 30)
    
    potentially_vulnerable_code()
    print("-" * 30)
    
    print("Test completed.")

if __name__ == "__main__":
    main()
