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
    
    potentially_vulnerable_code()
    print("-" * 30)
    
    print("Test completed.")

if __name__ == "__main__":
    main()
